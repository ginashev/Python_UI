from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_name1", header="group_head1", footer="group_foot1"))
    app.group.modify_first_group(Group(name="group_name2", header="group_head2", footer="group_foot2"))


def test_modify_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_name1", header="group_head1", footer="group_foot1"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group_name1", header="group_head1", footer="group_foot1"))
    app.group.modify_first_group(Group(header="New header"))

