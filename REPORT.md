
Because I am having trouble creating a virtualenv with python2, I am using python 3.6.1.
AUTH_PASSWORD_VALIDATORS only runs when Debug is false. This is so that you dont have do
go through hoops to create a user for testing.

Tried to prefetch_related('user') then .object_list.distinct('user')) but got an error. DISTINCT ON fields is not supported by this database backend