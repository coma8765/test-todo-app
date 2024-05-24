from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Task

api = Namespace("tasks", description="Tasks operations")

task_model = api.model(
    "Task",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "title": fields.String(required=True, description="The task title"),
        "description": fields.String(description="The task description"),
        "created_at": fields.DateTime(
            readonly=True, description="The task creation timestamp"
        ),
        "updated_at": fields.DateTime(
            readonly=True, description="The task update timestamp"
        ),
    },
)


@api.route("/")
class APITaskList(Resource):
    @api.doc("list_tasks")
    @api.marshal_list_with(task_model)
    def get(self):
        """List all tasks"""
        tasks = Task.query.all()
        return tasks

    @api.doc("create_task")
    @api.expect(task_model)
    @api.marshal_with(task_model, code=201)
    def post(self):
        """Create a new task"""
        data = api.payload
        task = Task(title=data["title"], description=data.get("description"))
        db.session.add(task)
        db.session.commit()
        return task, 201


@api.route("/<int:id>")
@api.response(404, "Task not found")
@api.param("id", "The task identifier")
class APITask(Resource):
    @api.doc("get_task")
    @api.marshal_with(task_model)
    def get(self, id):
        """Fetch a task given its identifier"""
        task = Task.query.get_or_404(id)
        return task

    @api.doc("update_task")
    @api.expect(task_model)
    @api.marshal_with(task_model)
    def patch(self, id):
        """Update a task given its identifier"""
        task = Task.query.get_or_404(id)
        data = api.payload
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        db.session.commit()
        return task

    @api.doc("delete_task")
    @api.response(204, "Task deleted")
    def delete(self, id):
        """Delete a task given its identifier"""
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return "", 204
