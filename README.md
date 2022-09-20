RishatTestStripe is an app created for the Stripe service testing purposes.
How to install the app locally:
- clone the repo,
- create a virtual environment for this project,
- install packages included in 'requirements.txt',
- execute command "py manage.py loaddata db.json" to deploy MySQL database.

To test the app using remote server, go to <a href="http://cdcollectionsale.site/index">cdcollectionsale</a>,
choose an item and push the button 'Buy'. When Stripe window opens,
enter an email, type '4242 4242 4242 4242' (credit card number field)
and any data later than this month (card expiry date). CVV/CVC code may include
any numbers, card holder name also may contain any name.
