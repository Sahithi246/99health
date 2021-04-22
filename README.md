# 99health
This is a simple django server where we can keep track of our tasks. When we run this server then a form will display saying to enter your task(Create) and after entering 
your task will be successfully stored in database(Postgresql) by creating unique id for it. 
When we give /all in the url then all the tasks will be displayed in json format.
when we give /update/id/ in the url then a form will appear saying update the record and after submitting it the record will be successfully submitted.
When we give /delete/id then data corresponding to that id will be deleted.
When we give /show/id in the url then data corresponding to that id will be displayed.

