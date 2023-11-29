import os
from datetime import datetime

from elasticsearch import Elasticsearch
from minio import Minio

blacklist = set()

def elastic_init():
    es = Elasticsearch([str(os.environ.get("ELASTIC_URI"))])

    return es

def is_token_blacklisted(access_token, current_user):
    es = elastic_init()
    
    index_name = 'blacklist'

    try:
        search = es.get(index=index_name, id=current_user)
        source_data = search['_source']
        stored_access_token = source_data.get('access_token')
        return stored_access_token == access_token
    except Exception as e:
        print(f"Error: {e}")
        return False
    # return access_token in blacklist


def add_blacklist(access_token, current_user):
    es = elastic_init()
    
    index_name = 'blacklist'

    # Periksa apakah indeks "blacklist" sudah ada
    if not es.indices.exists(index=index_name):
        # Jika belum ada, buat indeks tersebut
        es.indices.create(index=index_name)
    else:
        # Simpan token ke Elasticsearch
        es.index(index=index_name, id=current_user, document={
            'access_token': access_token,
            'timestamp': datetime.now()
        })
    # blacklist.add(access_token)
    print(f'Token {access_token} added to blacklist.')


def generate_sequence(model=None, code_attribute='', prefix=''):
    last_record = model.query.order_by(model.id.desc()).first()

    if last_record:
        last_sequence = getattr(last_record, code_attribute, '')
        # Menyaring karakter angka dari last_sequence
        last_number_str = ''.join(filter(str.isdigit, last_sequence))
        # Mengambil angka dari karakter angka terakhir
        last_number = int(last_number_str) if last_number_str else 0
        sequence_number = last_number + 1
    else:
        sequence_number = 1

    new_sequence = f'{prefix}{sequence_number:04}'
    return new_sequence

def minio_init():
    minio_endpoint = str(os.environ.get("MINIO_ENDPOINT"))
    minio_access_key = str(os.environ.get("MINIO_ACCESS_KEY"))
    minio_secret_key = str(os.environ.get("MINIO_SECRET_KEY"))

    minio = Minio(minio_endpoint, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

    return minio
