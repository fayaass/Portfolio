from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

# Create a Flask app instance
app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # You can use other mail servers like Outlook, etc.
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'muhammedfayas59504@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'fwqgcfqmqnajyfts'  # Replace with your email password or an app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'muhammedfayas59504@gmail.com'  # Default sender address

# Initialize Flask-Mail
mail = Mail(app)

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define the about page route
@app.route('/about')
def about():
    return render_template('about.html')

# Define the projects page route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Define the contact page route with POST method to handle form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create the email message
        msg = Message(f"New message from {name}", recipients=["muhammedfayas59504@gmail.com"])  # Recipient email here
        msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send the email
            mail.send(msg)
            return redirect(url_for('contact_success'))  # Redirect to a success page after sending the email
        except Exception as e:
            print(f"Error sending email: {e}")
            return "Error sending email."

    return render_template('contact.html')

# Define the contact success page
@app.route('/contact/success')
def contact_success():
    return "Your message has been sent successfully!"

# Run the application on localhost:5000
if __name__ == '__main__':
    app.run(debug=True)











# .project-item1{
#     background-image: url(../static/images/hublot\ background.webp);
#     background-size: cover; 
#     background-position: center center; 
#     background-repeat: no-repeat; 
#     height: 30vh; 
#     margin: 0;
#     padding: 0;
#     color: yellow; 
    

#     background-color: rgba(0, 0, 0, 0.5); 
#     padding: 20px;
#     border-radius: 10px;
# }

