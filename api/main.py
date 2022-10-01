import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from db import session
from model import User, UserTable
from schemas.queries import Queries

schema = strawberry.Schema(query=Queries)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


# ユーザー情報一覧取得
@app.get("/test_users")
def get_user_list():
    users = session.query(UserTable).all()
    return users


# ユーザー情報取得(id指定)
@app.get("/test_users/{user_id}")
def get_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user_id).first()
    return user


# ユーザ情報登録
@app.post("/test_users")
def post_user(user: User):
    db_test_user = User(name=user.name, email=user.email)
    session.add(db_test_user)
    session.commit()


# ユーザ情報更新
@app.put("/test_users/{user_id}")
def put_users(user: User, user_id: int):
    target_user = session.query(UserTable).filter(UserTable.id == user_id).first()
    target_user.name = user.name
    target_user.email = user.email
    session.commit()
