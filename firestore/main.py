
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "/Users/sumitkushwah/Downloads/todo-8370f-firebase-adminsdk-e3kbo-d58dd2e26e.json"
    )
firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# doc_ref = db.document(u'users/aaaaaa')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1913,
#     u'age': {
#         u'first': u'Alan',
#         u'middle': u'Mathison',
#         u'last': u'Turing',
#         u'born': 1913
#     }
# })

# users_ref = db.collection(u'users')
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

