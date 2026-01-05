⚖️ The "Is It Worth It?" Calculator
I built this app to solve a problem I (and probably most people) deal with all the time: Is it actually worth driving further away just to get a better price on something?

Sometimes we see a deal at a store across town, but by the time we pay for gas and spend an hour in traffic, we might actually be losing money. This calculator does the math for you so you know exactly when to go and when to stay home.

🚀 What it does:

Real-time Traffic: Uses the Google Maps API to get your actual driving time based on current traffic.

Fuel Math: Calculates exactly how much gas money you'll spend based on your car's MPG.

Time is Money: Lets you factor in your hourly wage as an "opportunity cost."

Interactive Map: Shows you the exact route you'll be taking.

The Verdict: Gives you a clear "Worth It" or "Stay Home" message based on your total expenses.

🛠️ How it works:

Enter your car's MPG and the current gas price.

(Optional) Toggle your hourly wage if you want to count your time as an expense.

Type in your Starting Address and your Destination.

Enter how much you expect to save at that destination.

Hit Calculate to see the map, the cost breakdown, and the final math!

💻 Tech Stack:

Streamlit: For the interactive web interface.

Google Maps API: (Distance Matrix, Geocoding, and Maps Embed) for the location data and routing.

Pandas: To organize the cost breakdown table.