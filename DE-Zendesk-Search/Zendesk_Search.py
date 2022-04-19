import sys
import pandas as pd


def populate_org_dict(target_df):
    result = {}

    for i in range(len(target_df)):
        org_id = target_df.loc[i, 'organization_id']
        org_id = int(org_id) if not pd.isnull(org_id) else 0

        if org_id in result:
            result[org_id] += ', ' + str(target_df.loc[i, '_id'])
        else:
            result[org_id] = str(target_df.loc[i, '_id'])
    return result


def generate_org_full_table(ticket_dict, user_dict):
    try:
        df_ticket_dict = pd.DataFrame(ticket_dict.items(), columns=['_id', 'tickets'])
        df_user_dict = pd.DataFrame(user_dict.items(), columns=['_id', 'users'])

        return pd.merge(pd.merge(df_orgs, df_ticket_dict, how='left', on='_id'), df_user_dict, how='left', on='_id')
    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        return False


def is_to_quit(input_val):
    if input_val == 'quit':
        print('Quit the Zendesk Search progress ...\n')
        sys.exit(0)


def get_searchable_fields():
    separator = '\n--------------------\n'
    output_msg = separator + 'Search Users with\n' + '\n'.join(list(df_users.columns))
    output_msg += separator + 'Search Tickets with\n' + '\n'.join(list(df_tickets.columns))
    output_msg += separator + 'Search Organizations with\n' + '\n'.join(list(df_orgs.columns))
    print(output_msg + '\n')


def show_main_instructions():
    input_2 = input('Select 1) Users or 2) Tickets or 3) Organizations\n')
    is_to_quit(input_2)

    while input == 'quit' or not int(input_2) in range(1, 4):
        is_to_quit(input_2)
        input_2 = input('Select 1) Users or 2) Tickets or 3) Organizations or type \'quit\' to exit \n')

    input_3 = input('Enter search term\n')
    is_to_quit(input_3)

    input_4 = input('Enter search value\n')
    is_to_quit(input_4)

    # TO-DO: Grab the input 2, 3, 4 values to start search and return the results


def init_instructions():
    print('Welcome to Zendesk Search\n')

    try:
        input_0 = input('Type \'quit\' to exit at any time, Press \'Enter\' to continue\n')
        is_to_quit(input_0)

        input_1 = input('''
                Select search options:
                    * Press 1 to search Zendesk
                    * Press 2 to view a list of searchable fields
                    * Type \'quit\' to exit\n''')
        is_to_quit(input_1)

        if int(input_1) == 1:
            show_main_instructions()
        elif int(input_1) == 2:
            get_searchable_fields()

            input_1_1 = input('Press \'Enter\' to the main steps, or type \'quit\' to exit\n')
            is_to_quit(input_1_1)
            show_main_instructions()
    except SyntaxError:
        pass


if __name__ == "__main__":
    print('Start loading local DB ...\n...\n...')

    df_tickets = pd.read_json('tickets.json')
    df_users = pd.read_json('users.json')
    df_orgs = pd.read_json('organizations.json')

    org_to_tkt_dict = populate_org_dict(df_tickets)
    org_to_user_dict = populate_org_dict(df_users)

    df_orgs_full = generate_org_full_table(org_to_tkt_dict, org_to_user_dict)
    # print(df_orgs_full[['_id', 'tickets', 'users']])

    print('Local DB loading completed!\n\n')

    init_instructions()
