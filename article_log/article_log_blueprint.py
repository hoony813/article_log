from flask import Blueprint

article_log_blueprint = Blueprint("article_log",__name__,static_folder="./static",template_folder="./templates")