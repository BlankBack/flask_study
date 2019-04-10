In [1]: from db_demo import *

In [2]: role = Role(name='admin')

In [3]: db.session.add(role)

In [4]: db.session.commit()

In [5]: user = User(name='heima', role_id=role.id)

In [6]: db.session.add(user)

In [7]: db.session.commit()

In [8]: user.name = 'chengxuyuan'

In [9]: db.session.commit()
e:\python_flask\flask_01\venv\lib\site-packages\pymysql\cursors.py:170: Warning: (1265, "Data truncated for column 'name' at row 1")
  result = self._query(query)

In [10]:  db.session.delet(user)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-10-0cce46b75cc2> in <module>
----> 1 db.session.delet(user)

AttributeError: 'scoped_session' object has no attribute 'delet'

In [11]:  db.session.delete(user)

In [12]: db.session.commit()

In [13]:
