# Import streamlit library
import streamlit as st 

# For data manipulation
import pandas as pd 

# Import time module for operations related to time; delay code execution
import time 

# Import os module, interact with os functions; read/write files
import os

# Import image class from Pillow (PIL) library; open, save image
from PIL import Image

# Provides date and time functions
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="UTP ParcelHub", page_icon=":package:", layout="centered")


# Initialize session state if not already set
if 'page' not in st.session_state:
    st.session_state.page = 'splash_screen'

# Define a placeholder for dynamic content
placeholder = st.empty()

# Splash Screen

# Checks if the value of st.session_state.page is set to 'splash_screen'
if st.session_state.page == 'splash_screen':
    st.markdown("""
        <style>
        .stApp { background-color: #F1F0EC; }
        .centered-content {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
            text-align: center;
        }
        h1 { text-align: center; color: #344EAD; }
        p { text-align: center; color: #000000; }
        </style>
    """, unsafe_allow_html=True)

    # Display the splash screen content
    with placeholder.container():
        st.markdown("""
            <div class="centered-content">
                <h1>UTP<br>ParcelHub</h1>
                <p>By student for students</p>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(3)  # Show splash screen for 3 seconds
        st.session_state.page = 'landing'  # Switch to landing page
        placeholder.empty()  # Clear the splash screen

# Landing Page
if st.session_state.page == 'landing':
    placeholder.empty()  # Ensure placeholder is cleared before rendering landing page
    with placeholder.container():
        st.markdown("""
        <style>
        .stApp {
            background-color: #F1F0EC;
        }
        .stButton > button {
            background-color: #091F5B;
            color: white !important;
            font-weight: bold;
            font-size: 50px;
            width: 100%;
            height: 80px;
            padding: 20px;
            border-radius: 10px;
            cursor: pointer;
            border: none;
        }
        .stButton > button:hover {
            opacity: 0.9;
        }
        </style>
        """, unsafe_allow_html=True)

        # Layout: Two columns for buttons
        col1, col2 = st.columns([1, 1])

        # Button for "UTP Student & Staff" navigation
        with col1:
            if st.button('UTP Student & Staff'):
                st.session_state.page = 'user_detail'  # Set page to parcel hub sign up page
                placeholder.empty()  # Clear the landing page before rendering the new one

        # Button for "Parcel Hub Admin" navigation
        with col2:
            if st.button('Parcel Hub Admin'):
                st.session_state.page = 'ph_sign_in'  # Set page to 'parcel_hub'
                placeholder.empty()  # Clear the landing page before rendering the new one
        
        # Additional Button for "Parcel Bro Admin"
        if st.button('Parcel Bro Admin'):
            st.session_state.page = 'pb_sign_in'  # Set page to 'parcel_bro'
            placeholder.empty()  # Clear the landing page before rendering the new one

# Define directory and file path
if st.session_state.page == 'user_detail':
    placeholder.empty()
    with placeholder.container():
    
        DIRECTORY = 'data'
        csv_file_path = os.path.join(DIRECTORY, 'user_data.csv')

        # Check if directory exists, and create it if it doesn't
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)  # Create directory
            
        # Print the absolute path to the CSV file
        st.write("CSV File Path:", os.path.abspath(csv_file_path))

        # Initialize session state
        if 'name' not in st.session_state: 
            st.session_state.name = None
        if 'address' not in st.session_state:
            st.session_state.address = None
        if 'phoneNum' not in st.session_state:
            st.session_state.phoneNum = None
            
        if st.session_state.page == 'user_detail':
            placeholder.empty()
            with placeholder.container():
                st.markdown("""
                <style>
                .stApp {
                    background-color: #F1F0EC;
                }
                h2 {
                    text-align: left;
                    color: #344EAD;      
                }
                p {
                    text-align: left;
                    color: #000000;
                }
                .stButton button {
                    color: #ffffff;  
                    background-color: #d8a15d;
                    display: flex;
                    justify-content: center;
                    border-radius: 8px;
                    padding: 5px 60px;
                    font-size: 18px;
                    border: 1px solid transparent;
                    display: flex;
                    justify-content: center;
                    margin: auto;
                }
                .stButton button:hover {
                    background-color: #B99058;
                    border: 1px solid white;
                    color: white;
                }    
                </style>
                """, unsafe_allow_html=True)
                
                st.markdown('<h2>Personal Details</h2>', unsafe_allow_html=True)
                st.markdown('<p>Get yourself started with Parcel Hub! Fill in the details below.</p>', unsafe_allow_html=True)

                # Input fields for user data
                name = st.text_input("Name", "Enter name on parcel")
                phoneNum = st.text_input("Phone Number", "Enter your Phone Number")
                
                st.divider()

                # Title 
                st.markdown('<h2>Address</h2>', unsafe_allow_html=True)
                st.markdown('<p>Kindly select your address for delivery purposes. </p>', unsafe_allow_html=True)

                # Define the selectboxes for each V
                V1 = st.selectbox("V1 options", ["V1", "V1A", "V1B", "V1C"], index=None)
                V2 = st.selectbox("V2 options", ["V2", "V2A", "V2B", "V2C"], index=None)
                V3 = st.selectbox("V3 options", ["V3", "V3A", "V3B", "V3C", "V3D", "V3E", "V3F"], index=None)
                V4 = st.selectbox("V4 options", ["V4", "V4A", "V4B", "V4C", "V4D", "V4E"], index=None)
                V5 = st.selectbox("V5 options", ["V5", "V5A", "V5B", "V5H", "V5K"], index=None)
                V6 = st.selectbox("V6 options", ["V6", "V6A", "V6B"], index=None)
                others = st.text_input("Others", "Your preferred address (if not listed)")

                selected_value = None
                if V1 != "Select an option" and V1:
                    selected_value = V1
                elif V2 != "Select an option" and V2:
                    selected_value = V2
                elif V3 != "Select an option" and V3:
                    selected_value = V3
                elif V4 != "Select an option" and V4:
                    selected_value = V4
                elif V5 != "Select an option" and V5:
                    selected_value = V5
                elif V6 != "Select an option" and V6:
                    selected_value = V6
                elif others:
                    selected_value = others

                if selected_value:
                    st.write(f"You selected: {selected_value}")
                    st.session_state['address'] = selected_value

                    if st.button("Continue"):
                        st.session_state.name = name
                        st.session_state.phoneNum = phoneNum
                        st.session_state.address = selected_value
                        
                        user_data = {
                            "Name": [name],
                            "Phone Number": [phoneNum],
                            "Address": [selected_value]  
                        }
                        
                        df = pd.DataFrame(user_data)
                        
                        # Define CSV file path
                        csv_file_path = 'user_data.csv'
                        
                        # Debug: Display the data being saved
                        st.write("Data to be saved:", df)

                        # Attempt to save data to CSV file with error handling
                        try:
                            if os.path.exists(csv_file_path):
                                df.to_csv(csv_file_path, mode='a', index=False, header=False)  # Append without header
                            else:
                                df.to_csv(csv_file_path, index=False)  # Create new file with header
                            st.success("Details saved successfully!")
                        except Exception as e:
                            st.error(f"Error saving details: {e}")
                            
                        placeholder.empty()
                        st.session_state.page = 'home'

            
# Home Page
if st.session_state.page == 'home': 
    placeholder.empty()  # Ensure landing page is cleared      
    with placeholder.container():
        st.markdown("""
        <style>
            .stApp {
                background-color: white;
            }
            
            h2, h3, h4, h5 {
            color: #091F5B;  
            }
            
            .text {
                color: black;
            }
            .stButton > button {
                background-color: #091F5B;
                color: white; 
                font-weight: bold;
                font-size: 20px;
                width: 100%;
                height: 80px;
                padding: 20px;
                border-radius: 10px;
                cursor: pointer;
                border: none;
            }
            .stButton > button:hover {
                opacity: 0.9;
            }
        </style>
        """, unsafe_allow_html=True) 
              
        st.markdown('<h2 class="header">Welcome, {}</h2>'.format(st.session_state.name), unsafe_allow_html=True)
        st.image("C:/Users/Ainin Sofiya/Documents/UTP/YEAR 3/FYP I/Images/holiday_notice_image.png.png")  # Ensure the path is correct
        st.markdown('<h5 class="header">Current Address: {}</h5>'.format(st.session_state.address), unsafe_allow_html=True)

        left_col, right_col = st.columns([1, 1])
        with left_col:
            if st.button("Information"):
                st.session_state.page = 'information'  # Navigate to 'information' page
                placeholder.empty()

        with right_col:
            if st.button("Delivery"):
                st.session_state.page = 'delivery'  # Navigate to 'delivery' page
                placeholder.empty()

        if st.button("Parcel Availability"):
            st.session_state.page = 'parcel_availability'  # Navigate to 'parcel_availability'
            placeholder.empty()


        if st.button("Need Help? Reach out to us."):
            st.session_state.page = 'cust_service'  # Navigate to 'cust_service'
            placeholder.empty()
        
        if st.button('Back'):
           st.session_state.page = 'landing'  # Set page to 'landing' page
            
            
# Information Page           
if st.session_state.page == 'information':
    placeholder.empty()  # Ensure Home page is cleared
    with placeholder.container():
        st.markdown("""
        <style>
        /* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
                
        /* Global text color to blue */
        h1 {
            color: #344EAD !important;
        }
        
        h2, h3, h4, p {
            color: #000000;
        }
    
        .stButton > button {
            background-color: #344EAD ;
            color: white; !important;
        }
        </style> 
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([8,1])
        
        with col1:
            # Folder where images are stored
            UPLOAD_DIR = "announcement_images"
            ANNOUNCEMENT_FILE = "announcement.txt"

            st.title("Information")

            # Display the latest announcement
            st.subheader("Important Announcement")

            if os.path.exists(ANNOUNCEMENT_FILE):
                with open(ANNOUNCEMENT_FILE, "r") as f:
                    announcement = f.read()
                if announcement:
                    st.write(announcement)
                else:
                    st.write("No announcements at the moment.")
            else:
                st.write("No announcement posted yet.")


            # Check if the folder has any images
            if os.path.exists(UPLOAD_DIR):
                image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

                if image_files:
                    for image_file in image_files:
                        image = Image.open(os.path.join(UPLOAD_DIR, image_file))
                        st.image(image, use_column_width=True)
                else:
                    st.write("No images uploaded yet.")
            else:
                st.write("No images folder found.")
        
        with col2:
            if st.button('Close'):
                st.session_state.page = 'landing'  # Set page to 'landing' page

if st.session_state.page == 'delivery':
    placeholder.empty() # Clear home page content
    with placeholder.container():
        # Custom CSS to style the page
        st.markdown("""
        <style>
            /* Set the background color of the main container */
            .main {
                background-color: white;
                padding: 10px;
            }
            
            /* Global text color to black */
            h1, h4, h5, h6, p, label, span {
                color: #000000 !important;
            }
            
            h2, h3 {
                color: #344EAD;
            }

            /* Reduce gap between radio buttons and subheaders */
            div[role='radiogroup'] {
                margin-top: -30px; /* Adjust the top margin to reduce space */
            }

            /* Custom button styling for all buttons */
            .stButton > button {
                background-color: #d8a15d !important;
                color: white !important;
                border: none !important;
                font-size: 1.5rem !important;
                cursor: pointer !important;
                width: 100px !important;
                height: 40px !important;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2) !important;
                transition: background-color 0.3s ease !important;
            }

            .stButton > button:hover {
                background-color: #c2924d !important;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([8, 1])
        
        with col1: 
            # Quantity of Parcel
            st.subheader("Quantity of Parcel")
            st.write("Enter the number of parcels to be collected")
            quantity = st.radio("", ['1', '2', '3', 'Others:'])
            if quantity == 'Others:':
                other_quantity = st.text_input("Specify other quantity")
            else:
                other_quantity = None

            # Parcel arrival dates
            st.subheader("Earliest & Latest Parcel Arrival Dates")
            st.write("If you have only one parcel, choose the same date for both the earliest and latest dates.")
            earliest_date = st.date_input("Earliest Date")
            latest_date = st.date_input("Latest Date")

            # Tracking Number
            st.subheader("Tracking Number")
            st.write("Note: If you have a parcel that arrived today or is still 'out for delivery', please put it in the bracket")
            st.write("Example:\nSPXM09255252 (Out for Delivery)\nSPX12984933 (Today)")
            tracking_number = st.text_area("Enter your tracking number")

            # Fragile Parcel
            st.subheader("Fragile Parcel")
            fragile = st.radio("", ['Yes', 'No'])

            # Parcel Items
            st.subheader("What Items are in Your Parcel")
            items = st.text_input("Enter item details")

            # Parcel categories
            st.markdown("<h3>Parcel Categories, Weight, and Price Details</h3>", unsafe_allow_html=True)
            st.markdown("<p>Parcel Hub categorizes and labels your parcels according to size and weight, starting with the smallest as 'K' and moving up to A, B, C, D, and finally E (>12kg).</p>", unsafe_allow_html=True)
            categories = st.multiselect("Select applicable categories:", ['K (Small Parcels)', 'A & B (<1kg)', 'C (2kg-3kg)', 'D (3kg)', 'E (>3kg)'])
            
            # Schedule Deliveries
            st.markdown("<h3>Today's Delivery</h3>", unsafe_allow_html=True)
            st.markdown("<p>Please choose the delivery time slot convenient to you</p>", unsafe_allow_html=True)
            delivery_slot = st.radio("",["SLOT E [7.30PM-10.45PM]", "SLOT F [9.45PM-11.59PM]"])     
            
            # Payment 
            st.write("For PAYMENT, please wait for the Payment Department to send you the QR code and payment details.")   
    
            st.write("")
            st.write("")

            # Center the "Done" button using three columns
            colA, colB, colC = st.columns([4, 1, 4])
            with colB:
                if st.button("Done"):
                    # Create a dictionary of the inputs
                    user_data = {
                        "Name": st.session_state.name,
                        "Phone Number": st.session_state.phoneNum,
                        "Address": st.session_state.address,
                        "Quantity of Parcel": quantity if quantity != 'Others:' else other_quantity,
                        "Earliest Date": earliest_date,
                        "Latest Date": latest_date,
                        "Tracking Number": tracking_number,
                        "Fragile": fragile,
                        "Items in Parcel": items,
                        "Parcel Categories": ', '.join(categories),
                        "Delivery Slot": delivery_slot
                    }

                    # Convert the dictionary to a DataFrame
                    df = pd.DataFrame([user_data])

                    # Define CSV file path
                    csv_file_path = 'user_parcel_data.csv'

                    # Check if file exists, append if it does, otherwise create a new one
                    if os.path.exists(csv_file_path):
                        df.to_csv(csv_file_path, mode='a', index=False, header=False)
                    else:
                        df.to_csv(csv_file_path, index=False)

                    # Display success message
                    st.session_state.page = 'home'
                    
        with col2: 
            if st.button('Back'):
                st.session_state.page = 'home'  # Set page to 'landing' page

if st.session_state.page == 'parcel_availability':
    placeholder.empty()
    with placeholder.container():
        
        col1, col2 = st.columns([8, 1])
        
        with col1:
            # Directory and file setup
            PARCEL_FILE_PATH = "parcel_data.csv"

            # Load parcel data
            def load_parcel_data():
                if os.path.exists(PARCEL_FILE_PATH):
                    return pd.read_csv(PARCEL_FILE_PATH)
                else:
                    return pd.DataFrame(columns=["Tracking Number", "Status", "Arrival Date" "Collection Date", "Image File"])

            # Customer tracking interface
            st.title("Parcel Tracking")
            st.subheader("Enter Tracking Number")

            tracking_num = st.text_input("Parcel Tracking Number")

            if st.button("Check Status"):
                if tracking_num:
                    df = load_parcel_data()
                    parcel = df[df["Tracking Number"] == tracking_num]

                    if not parcel.empty:
                        arrival_date = parcel["Arrival Date"].values[0]
                        status = parcel["Status"].values[0]
                        collection_date = parcel["Collection Date"].values[0]
                        image_file = parcel["Image File"].values[0]
                        
                        st.write(f"**Arrival Date:** {arrival_date}")
                        st.write(f"**Status:** {status}")
                        st.write(f"**Collection Date:** {collection_date}")

                        if image_file and os.path.exists(os.path.join("announcement_images", image_file)):
                            st.image(os.path.join("announcement_images", image_file), caption=tracking_num, width=200)
                    else:
                        st.error("No parcel found with the provided Tracking Number.")
                else:
                    st.warning("Please enter a Tracking Number.")
                    
        with col2:
            if st.button('Close'):
                st.session_state.page = 'home'  # Set page to 'home' page
        
if st.session_state.page == 'cust_service':
    placeholder.empty()
    with placeholder.container():
        st.markdown("""
        <style>
        /* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
                
        /* Global text color to blue */
        h1 {
            color: #344EAD !important;
        }
        
        h2, h3, h4, p {
            color: #000000;
        }
    
        .stButton > button {
            background-color: #344EAD ;
            color: white; !important;
        }
        </style> 
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([8, 1])
        
        with col1: 
            # Directory and file setup
            CUST_SERVICE_FILE = "cust_service.txt"
            
            st.title("Customer Feedback")
            feedback = st.text_area("Please share your feedback or questions with us!")
            
            if st.button("Submit"):
                if feedback:  # Check if feedback is not empty
                    with open(CUST_SERVICE_FILE, "a") as f:  # Append feedback to the file
                        f.write(feedback + "\n")  # Write feedback with a newline
                    st.success("Thank you for your feedback!")  # Confirmation message
                else:
                    st.warning("Please enter feedback before submitting.")

            # Check if feedback file exists and display previous feedback
            if os.path.exists(CUST_SERVICE_FILE):
                st.subheader("Your Previous Feedback")
                with open(CUST_SERVICE_FILE, "r") as f:
                    current_feedback = f.readlines()  # Read all lines from the file
                for line in current_feedback:
                    st.write(line.strip())  # Display each line of feedback

            else:
                st.write("No feedback posted yet.")
        
        with col2: 
            st.write("")
            st.write("")
            if st.button('Close'):
                st.session_state.page = 'home'  # Set page to 'home' page


# Parcel Hub Admin Sign In Page
if st.session_state.page == 'ph_sign_in':
        placeholder.empty()
        with placeholder.container():
            st.markdown("""
            <style>
            .stApp {
                background-color: #F1F0EC;
            }
            h2 {
                text-align: left;
                color: #344EAD;      
            }
            p {
                text-align: left;
                color: #000000;
            }
            .stButton button {
                color: #ffffff;  
                background-color: #d8a15d;
                display: flex;
                justify-content: center;
                border-radius: 8px;
                padding: 5px 60px;
                font-size: 18px;
                border: 1px solid transparent;
                display: flex;
                justify-content: center;
                margin: auto;
            }
            .stButton button:hover {
                background-color: #B99058;
                border: 1px solid white;
                color: white;
            }    
            </style>
            """, unsafe_allow_html=True)
            
            st.markdown('<h2>Sign in</h2>', unsafe_allow_html=True)
            st.markdown('<p>Fill in the details below to sign in.</p>', unsafe_allow_html=True)

            # Input fields for user data
            uname = st.text_input("Username", "Enter username")
            password = st.text_input("Enter a password", type="password")
            
            if st.button("Next"):
                st.session_state.page = 'parcel_hub'
                
                ph_admin_data = {
                    "Username": uname,
                    "Password": password
                }
                
                # Convert the dictionary to a DataFrame
                df = pd.DataFrame([ph_admin_data])
                
                # Define CSV file path
                ph_data_path = 'ph_admin_data.csv'
                
                # Append to CSV if it exists, otherwise create a new file
                if os.path.exists(ph_data_path):
                    # If the file exists, append without adding the header again
                    df.to_csv(ph_data_path, mode='a', index=False, header=False)
                else:
                    # If the file does not exist, create it and include the header
                    df.to_csv(ph_data_path, index=False)
                
                # Confirm data saving
                st.success("User data saved successfully!")
                
                # Empty the placeholder to clear the current form
                placeholder.empty()
                st.session_state.page = 'parcel_hub'

# Parcel Hub Admin Page
if st.session_state.page == 'parcel_hub':
    placeholder.empty()  # Clear landing page content
    with placeholder.container():
        st.sidebar.title("Admin Pages")
        
        col1, col2 = st.columns([8, 1])
        
        with col1:
            # Create dropdown selection
            ph_admin_page = st.selectbox("Go to", ["Parcel Key-In", "Parcel Key-Out", "Content Management"])
            st.session_state.ph_admin_page = ph_admin_page  # Store selection in session state

            # Directory and file setup
            PARCEL_FILE_PATH = "parcel_data.csv"
            UPLOAD_DIR = "uploaded_images"
            ANNOUNCEMENT_FILE = "announcement.txt"
            
            # Ensure upload directory exists
            if not os.path.exists(UPLOAD_DIR): # If it doesn't exist, create one
                os.makedirs(UPLOAD_DIR)

            # Define functions for handling parcel data
            def load_parcel_data():
                if not os.path.exists(PARCEL_FILE_PATH):
                    df = pd.DataFrame(columns=["Tracking Number", "Phone Number", "Status", "Arrival Date", "Collection Date", "Image File"])
                    df.to_csv(PARCEL_FILE_PATH, index=False)
                return pd.read_csv(PARCEL_FILE_PATH, dtype={"Phone Number": str}) # load phone num as strings to avoid rounding or zeroes

            def save_parcel_data(data):
                data.to_csv(PARCEL_FILE_PATH, index=False)
                
            # Function to add new parcel to the CSV file
            def add_new_parcel(tracking_num, phone_num, arrival_date, image_file_name):
                df = load_parcel_data()
                new_data = pd.DataFrame({
                    "Tracking Number": [tracking_num],
                    "Phone Number": [phone_num],
                    "Status": ["Not Collected"],
                    "Arrival Date": [arrival_date],
                    "Collection Date": [""],
                    "Image File": [image_file_name]
                })
                df = pd.concat([df, new_data], ignore_index=True) # Add new data to the end of the existing parcel data
                save_parcel_data(df)
                st.success(f"Parcel added successfully! Tracking Number: {tracking_num}")


            # Parcel Key-In Section
            if st.session_state.ph_admin_page == "Parcel Key-In":
                st.title("Parcel Key-In")
                st.subheader("Add New Parcel")

                # Input fields for new parcel entry
                phone_num = st.text_input("Phone Number")
                tracking_num = st.text_input("Parcel Tracking Number")
                arrival_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Image uploader and camera
                uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
                
                # Button to open the camera
                open_camera = st.button("Open Camera")
                
                # Show the camera input only when the "Open Camera" button is clicked
                if open_camera:
                    captured_image = st.camera_input("Capture an image")

                # Add new parcel on submit
                if st.button("Submit New Parcel"):
                    
                    # If phone num and tracking num is filled, then set image_file_name to None
                    if phone_num and tracking_num:
                        image_file_name = None # Create a placeholder image_file_name
                        
                        # Handle image saving and naming
                        if uploaded_image: # If image is uploaded
                            image_file_name = f"{tracking_num}_{uploaded_image.name}" # Uses f-string to embed variables into strings; avoid duplications in file names
                            with open(os.path.join(UPLOAD_DIR, image_file_name), "wb") as f: 
                                f.write(uploaded_image.getbuffer())

                        elif 'captured_image' in locals() and captured_image is not None:
                            image_file_name = f"captured_{tracking_num}.png"
                            with open(os.path.join(UPLOAD_DIR, image_file_name), "wb") as f:
                                f.write(captured_image.getbuffer())

                        # Save parcel to CSV
                        add_new_parcel(tracking_num, phone_num, arrival_date, image_file_name)

                    else:
                        st.warning("Please fill all the fields.")


            # Parcel Key-Out Section
            elif st.session_state.ph_admin_page == "Parcel Key-Out":
                st.title("Parcel Key-Out")
                st.subheader("Mark Parcel as Collected")
                
                # Input field for parcel details (Tracking Number)
                tracking_num = st.text_input("Enter Parcel Tracking Number for Collection", "")
                
                # Button to mark parcel as collected
                if st.button("Confirm Collection"):
                    if tracking_num:
                        df = load_parcel_data()
                        parcel_index = df.index[df["Tracking Number"] == tracking_num].tolist()
                        
                        if parcel_index:
                            df.at[parcel_index[0], "Status"] = "Collected"
                            df.at[parcel_index[0], "Collection Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            save_parcel_data(df) 
                            st.success(f"Parcel with Tracking Number {tracking_num} marked as collected!")
                        else:
                            st.error("No parcel found with the provided Tracking Number.")


            # Content Management Section
            elif st.session_state.ph_admin_page == "Content Management":
                st.title("Content Management")
                st.subheader("Manage Images, Announcements, and more")
                
                # Upload Images Section
                with st.expander("Upload Images", expanded=True):
                    uploaded_files = st.file_uploader(
                        "Choose images to upload", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
                    )

                    if uploaded_files:
                        for uploaded_file in uploaded_files:
                            with open(os.path.join(UPLOAD_DIR, uploaded_file.name), "wb") as f:
                                f.write(uploaded_file.getbuffer())
                            st.success(f"Uploaded {uploaded_file.name} successfully!")

                # Post Announcements Section
                with st.expander("Post and Manage Announcements", expanded=True):
                    announcement = st.text_area("Write your announcement here:")

                    if st.button("Post Announcement"):
                        with open(ANNOUNCEMENT_FILE, "w") as f:
                            f.write(announcement)
                        st.success("Announcement posted successfully!")

                    if os.path.exists(ANNOUNCEMENT_FILE):
                        st.subheader("Current Announcement")
                        with open(ANNOUNCEMENT_FILE, "r") as f:
                            current_announcement = f.read()
                        st.write(current_announcement)

                        if st.button("Delete Announcement"):
                            os.remove(ANNOUNCEMENT_FILE)
                            st.success("Announcement deleted successfully!")
                    else:
                        st.write("No announcement posted yet.")

                # Manage Uploaded Images Section
                with st.expander("Manage Uploaded Images", expanded=True):
                    st.subheader("Uploaded Images")

                    if os.path.exists(UPLOAD_DIR):
                        image_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

                        if image_files:
                            for image_file in image_files:
                                st.write(f"Image: {image_file}")
                                st.image(os.path.join(UPLOAD_DIR, image_file), caption=image_file, use_column_width=True)

                            for image_file in image_files:
                                if st.button(f"Delete {image_file}", key=image_file):
                                    os.remove(os.path.join(UPLOAD_DIR, image_file))
                                    st.success(f"Deleted {image_file} successfully!")
                        else:
                            st.write("No images uploaded yet.")
                            
                
                # Manage Customer Feedback section 
                with st.expander("Manage Customer Feedback", expanded=True):
                    st.subheader("Customer Feedback")
                    
                    # Folder where the text is stored
                    CUST_SERVICE_FILE = "cust_service.txt"

                    if os.path.exists(CUST_SERVICE_FILE):
                        with open(CUST_SERVICE_FILE, "r") as f:
                            feedback = f.read()
                        if feedback:
                            st.write(feedback)
                        else:
                            st.write("No announcements at the moment.")
                    else:
                        st.write("No announcement posted yet.")
                            
        with col2: 
            st.write("")
            st.write("")
            if st.button('Back'):
                st.session_state.page = 'landing'  # Set page to 'landing' page

if st.session_state.page == 'pb_sign_in':
    placeholder.empty()
    with placeholder.container():
        st.markdown("""
        <style>
        .stApp {
            background-color: #F1F0EC;
        }
        h2 {
            text-align: left;
            color: #344EAD;      
        }
        p {
            text-align: left;
            color: #000000;
        }
        .stButton button {
            color: #ffffff;  
            background-color: #d8a15d;
            display: flex;
            justify-content: center;
            border-radius: 8px;
            padding: 5px 60px;
            font-size: 18px;
            border: 1px solid transparent;
            display: flex;
            justify-content: center;
            margin: auto;
        }
        .stButton button:hover {
            background-color: #B99058;
            border: 1px solid white;
            color: white;
        }    
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<h2>Sign in</h2>', unsafe_allow_html=True)
        st.markdown('<p>Fill in the details below to sign in.</p>', unsafe_allow_html=True)

        # Input fields for user data
        uname = st.text_input("Username", "Enter username")
        password = st.text_input("Enter a password", type="password")
        
        if st.button("Next"):
            st.session_state.page = 'parcel_hub'
            
            pb_admin_data = {
                "Username": uname,
                "Password": password
            }
            
            # Convert the dictionary to a DataFrame
            df = pd.DataFrame([pb_admin_data])
            
            # Define CSV file path
            pb_data_path = 'pb_admin_data.csv'
            
            # Append to CSV if it exists, otherwise create a new file
            if os.path.exists(pb_data_path):
                # If the file exists, append without adding the header again
                df.to_csv(pb_data_path, mode='a', index=False, header=False)
            else:
                # If the file does not exist, create it and include the header
                df.to_csv(pb_data_path, index=False)
            
            # Confirm data saving
            st.success("User data saved successfully!")
            
            # Empty the placeholder to clear the current form
            placeholder.empty()
            st.session_state.page = 'parcel_bro'

    
if st.session_state.page == 'parcel_bro':
    placeholder.empty()
    with placeholder.container():
        st.markdown("""
        <style>
        /* Set the background color of the main container */
        .main {
            background-color: white;
            padding: 10px;
        }
                
        /* Global text color to blue */
        h1 {
            color: #344EAD !important;
        }
        
        h2, h3, h4, p {
            color: #000000;
        }
    
        .stButton > button {
            background-color: #344EAD ;
            color: white; !important;
        }
        </style> 
        """, unsafe_allow_html=True)
        
        st.sidebar.title("Admin Pages")
        
        col1, col2 = st.columns([8, 1])
        with col1:
            st.title("Parcel Bro Admin Pages")
            st.write("Current data on parcel delivery")
            
            # Load the CSV file
            csv_file_path = 'user_parcel_data.csv'
            df = pd.read_csv(csv_file_path)

            # Display the CSV data in Streamlit
            st.write("Here is the CSV file data:")
            st.dataframe(df) 
            
        with col2:
            if st.button("Back"):
                st.session_state.page = 'landing'
