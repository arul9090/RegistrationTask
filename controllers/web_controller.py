from flask import Blueprint, redirect, render_template, session, url_for
from models import user_model
from services.auth_service import admin_required, login_required

web_bp = Blueprint("web", __name__)


@web_bp.get("/")
def index():
    if "user_id" in session:
        return redirect(url_for("web.dashboard"))
    return redirect(url_for("auth.login"))


@web_bp.get("/dashboard")
@login_required
def dashboard():
    if "users:read" in session.get("permissions", []):
        return redirect(url_for("web.admin_dashboard"))
    return redirect(url_for("web.profile"))


@web_bp.get("/admin")
@admin_required
def admin_dashboard():
    all_users = user_model.list_users()
    stats = {
        "total": len(all_users),
        "admins": sum(1 for user in all_users if "admin" in user["roles"]),
        "newest": all_users[0]["name"] if all_users else "-",
    }
    return render_template(
        "dashboard_admin.html",
        all_users=all_users,
        stats=stats,
        admin_name=session.get("name", "Admin"),
    )


@web_bp.get("/profile")
@login_required
def profile():
    user = user_model.find_by_id(session["user_id"])
    if not user:
        session.clear()
        return redirect(url_for("auth.login"))
    return render_template("dashboard_user.html", user=user_model.serialize_user(user))
