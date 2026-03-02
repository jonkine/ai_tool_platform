from fastapi import FastAPI
from app.router import router
app = FastAPI()
#注册路由
app.include_router(router)
if __name__ == "_main_":
    import uvicorn
    #启动服务
    uvicorn.run("app.main:app", host="127.0.0.1", post=8000, reload=True)
    