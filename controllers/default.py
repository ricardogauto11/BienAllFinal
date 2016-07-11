# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# ----------------------------------------------------------------------
import math

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """    
    return dict()

def dejaTuHuella():
    	form = SQLFORM(db.image)
    	if form.accepts (request.vars, session):
    		response.flash = 'Imagen cargada correctamente!'
    		redirect (URL ('default', 'galeria'))
    	return dict(form = form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


#@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def masApps():
    return dict()

def nosotros():
    return dict()

def galeria():
    """
    ipp = 6
    if len(request.args): page = int(request.args[0])
    else: page = 0
    ipp = 6
    limitby = (page*ipp, (page+1)*ipp+1)
    rows = db().select(db.image.ALL, limitby=limitby)
    return dict(galeria=galeria, rows=rows, page=page, ipp=ipp)
    """
    perpage = 6
    if not request.vars.page:
        redirect (URL(vars={'page':1}))
    else:
        page = int(request.vars.page)
    total = db(db.image.id > 0).count()
    pages = math.ceil(total // perpage)
    start = (page-1) * perpage
    end = page * perpage
    prev=page-1 if page > 0 else None
    prox=page+1 if page < pages else None
    if end > total:
        end = total
    galeria = db(db.image.id > 0).select(orderby=~db.image.id, limitby=(start, end))
    return dict(galeria=galeria,
        start=start,
        end=end,
        total=total,
        prev=prev,
        prox=prox,
        pages=pages)

def mostrarFoto():
    image = db.image(request.args(0, cast = int))
    db.comment.image_id.default = image.id
    form = SQLFORM(db.comment)
    if form.accepts(request.vars, session):
        redirect (URL('default', 'mostrarFoto', args=image.id))
    comments = db(db.comment.image_id==image.id).select()
    return dict (image=image, comments=comments, form=form)

def nombre():
    return dict(nombre = db().select(db.image.title))
