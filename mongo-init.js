db.auth('surveyadmin', 'mongoadmin')

db = db.getSiblingDB('survey')

db.createCollection('sample_collection');

db.createUser(
    {
        user: 'surveyadmin',
        pwd: 'mongoadmin',
        roles: [
            {
                role: 'readWrite',
                db: 'survey'
            }
        ]
    }
);