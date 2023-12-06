import time

from datetime import datetime

from flask import request
from flask_jwt_extended import get_jwt_identity

from app import response, db, executor
from app.handler import generate_sequence, send_email, elastic_init
from app.model.account import ts_account
from app.model.ticket import ts_ticket


def index():
    try:
        es = elastic_init()
        index_name = 'ticket_log'
        query = {
            "query": {
              "match_all": {}
            }
        }

        result = es.search(index=index_name, body=query)

        data = [hit['_source'] for hit in result['hits']['hits']]

        return response.success(data, 'Data has been retrieved!')

    except Exception as e:
        return response.error('', e)


def create():
    author = get_jwt_identity()

    creator = ts_account.query.filter_by(account_username=author).first()

    ticket_no = generate_sequence(model=ts_ticket, code_attribute='ticket_no', prefix='TC')
    ticket_subject = request.form.get('ticket_subject')
    ticket_type = request.form.get('ticket_type')
    ticket_status = request.form.get('ticket_status')
    ticket_priority = request.form.get('ticket_priority')
    ticket_author = author
    ticket_assignee = request.form.get('ticket_assignee')
    # ticket_finish_date = request.form.get('ticket_finish_date')
    ticket_estimed_time = request.form.get('ticket_estimed_time')
    ticket_progress = request.form.get('ticket_progress')
    ticket_desc = request.form.get('ticket_desc')
    # ticket_attachment = request.files('ticket_attachment')
    departement_code = request.form.get('departement_code')
    submission_by = author
    # process_date = request.form.get('process_date')
    process_by = author
    created_by = author

    es = elastic_init()
    index_name = 'ticket_log'

    try:
        if not all([
            ticket_no,
            ticket_subject,
            ticket_type,
            ticket_status,
            ticket_priority,
            ticket_author,
            ticket_assignee,
            ticket_progress,
            ticket_desc,
            departement_code,
            ticket_estimed_time
        ]):
            return response.error('', 'Incomplete data provided')

        model = ts_ticket(
            ticket_no=ticket_no,
            ticket_subject=ticket_subject,
            ticket_type=ticket_type,
            ticket_status=ticket_status,
            ticket_priority=ticket_priority,
            ticket_author=ticket_author,
            ticket_assignee=ticket_assignee,
            ticket_progress=ticket_progress,
            ticket_desc=ticket_desc,
            ticket_estimed_time=ticket_estimed_time,
            departement_code=departement_code,
            # ticket_attachment=ticket_attachment,
            submission_by=submission_by,
            created_by=created_by,
            process_by=process_by
        )

        ticket_log = {
            'ticket_no': ticket_no,
            'ticket_subject': ticket_subject,
            'ticket_type': ticket_type,
            'ticket_status': ticket_status,
            'ticket_priority': ticket_priority,
            'ticket_author': ticket_author,
            'ticket_assignee': ticket_assignee,
            'ticket_progress': ticket_progress,
            'ticket_desc': ticket_desc,
            'ticket_estimed_time': ticket_estimed_time,
            'departement_code': departement_code,
            'ticket_start_date': datetime.now(),
            'created_date': datetime.now(),
            'created_by': ticket_author
        }

        db.session.add(model)
        db.session.commit()

        recipients = creator.account_mail, 'zainalmos2008@gmail.com'
        subject = 'Supportify - Ticket Created'
        body = f"""
            <html>
                <head></head>
                <body>
                    <h2>{subject} - {ticket_no} - {ticket_type} - {ticket_priority}</h2>
                    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
                    when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                    It has survived not only five centuries, but also the leap into electronic typesetting, 
                    remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets 
                    containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus 
                    PageMaker including versions of Lorem Ipsum.</p>
                </body>
            </html>
        """

        unique_job_id = f"send_email_{int(time.time())}"
        executor.submit_stored(unique_job_id, send_email, subject, body, (recipients))

        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)
        else:
            log = es.index(index=index_name, id=model.id, document=ticket_log)
            executor.submit(log)

        return response.success(ticket_no, 'ticket has been created!')

    except Exception as e:
        return response.error('', e)
