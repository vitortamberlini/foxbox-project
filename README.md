# FoxBox Digital - Car Management System :car: :gear:

Hey there, savvy tech enthusiasts! 🚀 I'm excited to present to you a cool web application that's going to rev up your engines! It's a Car Management System, built exclusively for the **FoxBox Digital Python Engineer Challenge**.

This application was completed within a scorching timeline of just 3 days! But despite the speed, we took care of every detail and added some bonuses. Let's dive into the hood, shall we? 

## Technical Stack Used :wrench: 

- **Back-end Framework**: Django 
- **Database**: SQLite (for now, more on that later!) 
- **Front-end Styling**: Bootstrap 
- **Front-end Interactions**: Vanilla JS
- **Views**: Class-Based Views
- **Form Handling**: Django Form and Formsets 
- **Testing**: Pytest 

Bonus points: We even incorporated Docker settings to make this beast run smoothly! :whale:

## Application Features :blue_car: 

- An impressive **management panel** that lists all existing cars in a neat table, including their model, brand, color, value, production costs, and transportation costs.
- An **Add Car page** that lets you input all the details of a new car to be added to your fleet.
- An intuitive **Update feature** that turns the table into an editable format so you can change car details as and when you need. As you update the Production Costs or Transportation Costs, the total column automatically shows you the new total! 

## Run This Beauty :key: 

To get this application up and running on your local machine:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run `docker-compose up` to start the application. 

(For detailed installation instructions, check the Installation Guide below)

## Extras :gift: 

We didn't just stop at the requirements. We went above and beyond and implemented a CI pipeline with **GitHub Actions** using flake8 (for linting), black (for formatting), and pytest (for testing)!

## Follow-up Work :construction_worker:

Our race against time is over and we've crossed the finish line, but the thrill of the chase has given us some ideas for what could be done to supercharge this project even further if the pit stop were a bit longer:

- Implementing the **codecov bot** for an in-depth analysis of code coverage.
- Boosting our **code tests** to the gold standard of 100% coverage.
- Replacing SQLite with a robust, production-grade DB like **Postgres or MySQL**.
- Flexing our CRUD muscles and adding the functionality to **delete a Car** from the database.
- Fine-tuning the environment with **separate settings for development/production**.
- Streamlining dependencies with an auto-update feature for the **requirements.txt** based on the application's imports.
- Keeping our code clean and organized with a linter for importing libraries in **alphabetical order**.

These are some of the enhancements we envisioned for our Car Management System. Consider this our project wishlist, or a roadmap for future adventures in code!

## Testing :test_tube:

To test the app, use the following command:

```bash
pytest
```

So gear up, hold on to your seats, and get ready for a high-octane experience with our Car Management System. We built this baby with a lot of :heart: and :sweat_smile:. We hope you love it as much as we do!

Happy Coding! :computer: 

### To get this application up and running on your local machine:

1. Clone the repository: 

```bash
git clone https://github.com/<your-username>/foxbox-car-management.git
```

2. Navigate to the project directory:

```bash
cd foxbox-car-management
```

3. Start the application:

```bash
docker-compose up
```

That's it! The application should now be running at localhost:8000.

To stop the application, just use the following command:

```bash
docker-compose down
```
