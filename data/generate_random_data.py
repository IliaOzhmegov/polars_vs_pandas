import os
import csv
import uuid
import random
import datetime


def generate_users(num_users=10 ** 3):
    header = ['user_id', 'is_blocked']
    data   = [[uuid.uuid4(), random.random() < 0.2] for _ in range(num_users)]
    return {'header': header, 'data': data}


def generate_transactions(users, num_transactions=10 ** 6):
    header = [
        'transaction_id',
        'date',
        'transaction_amount',
        'transaction_category_id',
        'is_blocked',
        'user_id'
    ]

    data = [[
        uuid.uuid4(),
        (datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d'),
        '%.2f' % ((random.gammavariate(5, 1) * 100) - 500),
        int(random.betavariate(2, 5) * 10),
        random.random() < 0.99,
        random.choice(users["data"])[0]
    ] for i in range(num_transactions)]

    return {'header': header, 'data': data}


def write_data(out, header, data):
    if os.path.exists(out):
        print('File %s already exists!' % out)
        return False

    try:
        with open(out, 'w') as f:
          writer = csv.writer(f)
          writer.writerow(header)
          writer.writerows(data)
    except Exception as err:
        print('Failed to write %s' % out)
        return False
    return True


if __name__ == '__main__':
    users = generate_users()
    transactions = generate_transactions(users)

    write_data('users.csv',               users['header'],        users['data'])
    write_data('transactions.csv', transactions['header'], transactions['data'])
