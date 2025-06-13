from readdocs.api.routers import document_router

def include_routers(app):
    app.include_router(document_router.router)
