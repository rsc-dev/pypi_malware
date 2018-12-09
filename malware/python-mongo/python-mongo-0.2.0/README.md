mongo
=====

Minimalistic pymongo object wrapper


Document
--------

Minimal document model:

    >>> from mongo import Document, Index
    >>> class Doc(Document):
    ...     __database__ = 'mongo_test'  # database name


All allowed settings:

    >>> class Doc(Document):
    ...     __connection__ = {'host': 'localhost', 'port': 27017}
    ...     #__auth__ = ('username', 'password')
    ...     __database__ = 'mongo_test' # database name
    ...     __collection__ = 'test'     # collection name
    ...     __safe__ = True             # enable safe insert mode
    ...
    ...     __indexes__ = [
    ...         Index('number', unique=True, sparse=True),
    ...     ]


Clear collection
----------------

    >>> t = Doc.remove()
    >>> Doc.count()
    0


Create document
---------------
    
    >>> doc = Doc(foo='bar')
    >>> doc['number'] = 10
    >>> doc.save()
    >>> '_id' in doc
    True


Fetch
-----
Get by id:

    >>> doc1 = Doc.get_by_id(doc.id)
    >>> doc1 == doc
    True

Find one:

    >>> doc2 = Doc.find_one({'number': 10})
    >>> doc2 == doc
    True

Find:

    >>> doc3 = Doc.find({'number': 10}).limit(1)[0]
    >>> doc3 == doc
    True

Get or create:

    >>> doc4, new = Doc.get_or_create({'number': 10}, defaults={'foo': 'bar'})
    >>> new
    False
    >>> doc4 == doc
    True


Update
------

Update filtered documents:

    >>> t = Doc.update({'number': 10}, {'$set': {'text': 'foo'}})
    >>> doc = Doc.find_one({'number': 10})
    >>> doc['text']
    u'foo'

Save only some fields:

    >>> doc['text'] = u'bar'
    >>> doc['number'] = 11
    >>> doc.save_fields('text')
    >>> doc = Doc.find_one({'number': 10})
    >>> doc['text'], doc['number']
    (u'bar', 10)

Update only some fields:

    >>> doc.atomic_update({'$inc': {'number': 2}})
    >>> doc = Doc.find_one({'text': 'bar'})
    >>> doc['number']
    12


Counting
--------

    >>> Doc().save()
    >>> Doc.count()
    2
    >>> Doc.find({'number': 12}).count()
    1


Delete 
------

Remove single document:

    >>> t = doc.delete()
    >>> Doc.find_one({'number': 12})

Remove some documents:

    >>> t = Doc.remove({'number': 10})

Remove all documents:

    >>> t = Doc.remove()
