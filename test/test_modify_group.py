from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="group_name2", header="group_head2", footer="group_foot2"))
    app.session.logout()
