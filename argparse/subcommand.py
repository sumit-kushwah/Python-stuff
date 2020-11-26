import argparse

parser = argparse.ArgumentParser(prog="todo", description='A smart command line todo application.')
subparsers = parser.add_subparsers(title="subcommands", description='Available subcommands', help='commands', dest="subcommand")

# parser for add sub-command

parser_add = subparsers.add_parser('add', help="add one or more tasks")
parser_add.add_argument('tasks', nargs='+', help='task descriptions')
parser_add.add_argument('-p', '--project', help='project name')

# parser for list sub-command

parser_list = subparsers.add_parser('list', help='list out tasks')
listgroup = parser_list.add_mutually_exclusive_group()
listgroup.add_argument('-a', '--all', action='store_true', help='list out all tasks')
listgroup.add_argument('-d', '--due', action='store_true', help='list out overdue tasks')
listgroup.add_argument('-u', '--upcoming', action='store_true', help='list out upcoming tasks')
parser_list.add_argument('--sort', action='store_true', help='sort tasks by name, date etc.')
parser_list.add_argument('--verbose', '-v', action='count', help='verbosity label', default=0)

# parser for find sub-command

parser_find = subparsers.add_parser('find', help="find tasks by text or #label")
parser_find.add_argument('text', help="text or #label")

# parser for update sub-command

parser_update = subparsers.add_parser('update', help='update tasks description or project name')
updategroup = parser_update.add_mutually_exclusive_group()
updategroup.add_argument('-id', '--taskid', help='id of task')
updategroup.add_argument('-p', '--project', help='project name')

# parser for delete sub-command

parser_delete = subparsers.add_parser('delete', help='delete tasks or project')
deletegroup = parser_delete.add_mutually_exclusive_group()
deletegroup.add_argument('-id', '--taskid', help='id for task')
deletegroup.add_argument('-p', '--project', help='project name')

# parser for sync sub-command

parser_sync = subparsers.add_parser('sync', help='Sync tasks with firebase')

# parser for mail sub-command

parser_mail = subparsers.add_parser('mail', help='Mail tasks')
parser_mail.add_argument('--subject', help='Subject of mail message')

# parser for print sub-command

parser_print = subparsers.add_parser('print', help='Print tasks')
parser_print.add_argument('-f', '--filename', help='File name')

# parsing the arguments

args = parser.parse_args()