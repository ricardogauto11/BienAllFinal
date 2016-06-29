# -*- coding: utf-8 -*-

def index():
	return dict(index = db().select(db.image.archivo))

def mostrarFoto():
	image = db.image(request.args(1))
	return dict (image = image)

def nombre():
	return dict(nombre = db().select(db.image.title))

def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)