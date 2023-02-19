# Genesys_Test_Task
Coding Exercise
Part 1 - Create a simple user management and authentication system
The purpose of the exercise is to evaluate your ability to create a simple REST web service. This test is designed
to take no more than two hours to complete, though there is no predefined time limit.
Requirements:
• Create, Update, Delete, List web service endpoints for a user object.
• User object should contain a name, email address, password and the date of their last login.
• Provide a login endpoint that validates the email address and password provided by the user
matches the one stored in the database.
Notes:
• Please write your code in Python.
• You may choose any database you like (sqlite, mysql, mssql, mongodb, dynamodb, etc.)
• You don't need to worry about logging, deployment, https, etc.
• You do not need to worry about providing any kind of user interface.
• If there are any areas of the code that are left incomplete, provide good comments about how
you would implement missing features
• Code must be submitted to github or bitbucket, and must be done at least 24 hours prior to the interview.
• If you have questions or clarifications, please contact your recruiter.
During the interview, we will expect you to demo (Postman/curl or alternative) and discuss the code you submitted, so be prepared to talk in-depth about the implementation, enhancements, etc.

Part 2 - Architectural Analysis
Now let’s imagine that this service was integrated into a product and that it experienced wild
success. Put on your architecture hat and walk us through how your solution would perform as load
increases. What challenges would your service face as it ramped up to handle internet-scale load? How
would you respond?
The point of this exercise is to understand how you think about architecture and software design. We
are not expecting that your solution for part 1 will handle this load; we only want to use it as a starting
point for the discussion.
