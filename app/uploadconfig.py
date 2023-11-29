ALLOWED_EXTENTIONS = {'png', 'jpeg', 'jpg', 'pdf'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS
