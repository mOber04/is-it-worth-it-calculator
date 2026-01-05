import streamlit as st
import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key=st.secrets["GOOGLE_MAPS_KEY"])

st.title(" ⚖️ The 'Is It Worth It?' Calculator")
st.subheader("Calculate if the trip to get a cheaper price actually saves you money")

# Just spaces info out
st.write("")
st.write("")
st.write("")

# st.expander containerizes the slide bars
with st.expander("🚗 Vehicle & Wage Settings", expanded=True):
    #Including wage is an optional element
    wageApplied = st.toggle("Include my hourly wage in the cost?")
    if wageApplied:
        wage = st.slider("Hourly wage ($)", 0.0, 100.0, 25.0, 0.5)
    else:
        wage = 0.0

    mpg = st.slider("Car's MPG", 5.0, 50.0, 5.0, 0.5)
    gas_price = st.slider("Gas Price ($)", 1.0, 7.0, 1.0, 0.1)

# Just spaces info out
st.write("")
st.write("")
st.write("")

# Main area inputs
col1, col2 = st.columns(2)

with col1:
    start_point = st.text_input("Starting Address:", "UMBC, Baltimore, MD")
    savings = st.number_input("How much will you save? ($)", min_value=0.0, value=0.0)

with col2:
    destination = st.text_input("Destination Address:", "Target, Catonsville, MD")

# Calculations take place
if st.button("Calculate Real Cost"):

    if (start_point == "") or (destination == ""):
        st.info("Please enter your information into the designated boxes", icon="⚠️")
    else:

        # 1. Get the data from Google
        result = gmaps.distance_matrix(
            start_point,
            destination,
            mode='driving',
            departure_time='now',
            traffic_model='best_guess'
        )

        # 2. Extract distance and time
        if result['rows'][0]['elements'][0]['status'] == 'OK':


            # Note: You use the same API key here
            # The corrected URL for the Directions mode of the Embed API
            map_url = f"https://www.google.com/maps/embed/v1/directions?key={st.secrets['GOOGLE_MAPS_KEY']}&origin={start_point.replace(' ', '+')}&destination={destination.replace(' ', '+')}&mode=driving"

            # Use HTML to display it
            st.write("### Driving Route")
            st.components.v1.iframe(map_url, width=700, height=400)

            element = result['rows'][0]['elements'][0]

            #converts distance to miles
            dist_miles = element['distance']['value'] * 0.000621371

            traffic_data = element.get('duration_in_traffic', element['duration'])
            time_hours = traffic_data['value'] / 3600

            # 3. Perform the math (Round Trip)
            total_miles = dist_miles * 2
            total_time = time_hours * 2

            fuel_expense = (total_miles / mpg) * gas_price
            time_expense = total_time * wage
            total_expense = fuel_expense + time_expense
            final_benefit = savings - total_expense

            # 4. Show the Verdict
            st.divider()
            if final_benefit > 0:
                st.success(f"✅ **Worth it!** You still save **${final_benefit:.2f}** after expenses.")
            else:
                st.error(f"🏠 **Stay home.** This trip actually costs you **${abs(final_benefit):.2f}** more than you save.")

            # 5. Show the "Hidden Costs" breakdown
            st.write("### The Breakdown")
            stats = {
                "Metric": ["Round Trip Distance", "Total Driving Time", "Gas Money Spent", "Value of your Time"],
                "Value": [f"{total_miles:.1f} miles", f"{total_time * 60:.0f} mins", f"${fuel_expense:.2f}",
                          f"${time_expense:.2f}"]
            }
            st.table(pd.DataFrame(stats))

        else:
            st.warning("Google couldn't calculate that route. Check your addresses!")


if st.toggle("Show Formula's Used"):
    st.latex(r"\text{Fuel Cost} = \left( \frac{\text{Total Miles}}{\text{MPG}} \right) \times \text{Price per Gallon}")
    st.latex(r"\text{Time Cost} = \text{Total Time} \times \text{Hourly Wage}")
    st.latex(r"\text{Final Benefit} = \text{Savings} - (\text{Fuel Cost} + \text{Time Cost})")