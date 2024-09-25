from flask import Flask, render_template, redirect, url_for, request, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure this is set for session management

# Sample user data (for demonstration purposes)
users = {
    'admin': 'password'  # Replace with your actual authentication method
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are correct
        if username in users and users[username] == password:
            session['logged_in'] = True  # Set session variable
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Redirect to the dashboard on success
        else:
            flash('Invalid username or password', 'danger')  # Show error message on failure

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'logged_in' in session:
        return render_template('dashboard.html')  # Render your dashboard template here
    else:
        flash('You need to log in first!', 'danger')
        return redirect(url_for('login'))  # Redirect to login page if not logged in

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove the logged_in session variable
    flash('You have been logged out!', 'success')
    return redirect(url_for('login'))  # Redirect to the login page

if __name__ == '__main__':
    app.run(debug=True)
