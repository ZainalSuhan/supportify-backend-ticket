from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_executor import Executor

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

executor = Executor(app)


from app import routes
from app.model import account, account_privilege, company, company_client, departement, email, parameter, \
        parameter_detail, sla, teamsupport, teamsupport_client, ticket, ticket_log, ticket_message, temp_signin, \
        temp_signup, company_client_project, teamsupport_client_account