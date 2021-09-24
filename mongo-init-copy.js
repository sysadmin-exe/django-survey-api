db.auth('db_username', 'db_passwd')

db = db.getSiblingDB('db_name')

db.createCollection('sample_collection');

db.createUser(
    {
        user: 'db_username',
        pwd: 'db_passwd',
        roles: [
            {
                role: 'readWrite',
                db: 'db_name'
            }
        ]
    }
);