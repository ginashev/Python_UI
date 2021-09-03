from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="group_name2", header="group_head2", footer="group_foot2"))


def test_modify_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_header(app):
    app.group.modify_first_group(Group(header="New header"))

