# Blood Donation Project

## Overview

The Blood Donation Project is designed to serve as a hub for individuals in need of blood donors during emergencies and for those willing to help. The application includes user registration, profile management, blood donation requests, and an admin dashboard.

## Features

1. **User Authentication:**
   - **Registration:** Custom user model with email, active status, staff, and admin roles.
   - **Login:** Users must have a profile to log in. If no profile exists, users are redirected to profile creation.

2. **Profile Management:**
   - **Profile Viewing:** View personal profile details and blood donation requests.
   - **Profile Updating:** Update profile details with restrictions on changing blood type and availability based on the last donation date.

3. **Blood Donation CRUD:**
   - **Create Donation Request:** Users can create blood donation requests. If the request type is "donating," fields are auto-filled based on the user’s profile.
   - **Edit Donation Request:** Edit requests with a type of "looking."
   - **Delete Donation Request:** Users can delete their own donation requests.
   - **List and Detail Views:** View lists and details of blood donation requests with associated user profile information.

4. **Admin Dashboard:**
   - **Manage Requests:** Admins can create, edit, and delete blood donation requests.
   - **Manage Users:** Admins can edit and delete user accounts.

unfixable error, i give up (deleted database or smth)
