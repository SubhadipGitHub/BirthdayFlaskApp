# Birthday Countdown and Celebration App

This is a Flask application to celebrate your fiancée's birthday with a beautiful animated countdown, a love message, and a fun poll. The app transitions smoothly from a countdown page to a birthday celebration page with a sweet love letter and a GIF when the countdown ends. It also includes a poll to engage friends and family in sharing what they love most about her.

## Features

- **Animated Countdown**: Displays a beautiful countdown timer until the birthday.
- **Birthday Celebration**: Shows a love message and a GIF when the countdown ends.
- **Poll**: Allows users to vote on what they love most about the birthday person.
- **Poll Results**: Displays the results of the poll.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/birthday-app.git
    cd birthday-app
    ```

2. Create and activate a Conda environment:
    ```bash
    conda create --name flaskbirthday-env python=3.8
    conda activate flaskbirthday-env
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    flask run
    ```

## Usage

1. **Countdown Page**: The home page displays a countdown to the birthday.
2. **Poll Page**: Navigate to `/poll` to participate in the poll.
3. **Poll Results Page**: Navigate to `/poll_results` to see the poll results.

## File Structure


![File_Structure Screenshot](https://i.imgur.com/B9mSBXZ.png)

## Templates

- **base.html**: Base template that includes the navigation menu.
- **countdown.html**: Template for the countdown page.
- **poll.html**: Template for the poll page.
- **poll_results.html**: Template for the poll results page.

## Static Files

- **css/styles.css**: Contains the styles for the application.
- **js/countdown.js**: Contains the JavaScript for the countdown timer.

## Routes

- `/`: Home page with the countdown timer.
- `/poll`: Poll page to vote on favorite characteristics.
- `/poll_results`: Page to view the poll results.
- `/submit_poll`: Route to handle poll submission (POST).

## Poll Functionality

The poll allows users to vote for their favorite characteristic of the birthday person. The results are stored in a dictionary and displayed on the poll results page.

## Transition Animation

When the countdown ends, the application smoothly transitions from the countdown page to the birthday celebration page using CSS transitions.

## Dependencies

- Flask
- Jinja2

## Setup

### Prerequisites

- Docker installed on your machine.

### Steps to Run the Application

1. **Build the Docker image from the Dockerfile**

   ```sh
   docker build -t python-docker-birthdayapp .

2. **Run the docker image**
   ```sh
   docker container run -dit -p 80:80 python-docker-birthdayapp

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
