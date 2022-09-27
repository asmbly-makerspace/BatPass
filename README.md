# ATXHS BatPass

<hr>

# DEPRECATED - This project is no longer active

<hr>

Discourse thread at https://yo.atxhs.org/t/revamping-our-internal-systems/300

The vision – **all admin interactions with account(s) occur through the LDAP**. LDAP is the source of truth for all member info including active billing, B-share, contact info, etc (i.e. admins do not directly interact with subsystems like Freshbooks to update accounts). Accurate info, easily accessible.

## The needs described in this project have been largely satisfied by our new member management system Neon.  Work is now being redirected to Neon API integrations to achieve the workflows shown below.

Check out the Neon Integrations repo [here](https://github.com/ATXHS/NeonIntegrations) for the latest developments.
<br>
<hr>

Here's what the basic workflow would look like for the base model created which we can build further upon.
![BatPass workflow](/images/ATXHS_BatPass.png)

Link to Google drawing [here](https://docs.google.com/drawings/d/1yIYogNvRNthOQkoszzCV3sKi9nQr5vJnzmHsZl3sID4/edit?usp=sharing)
<br>
<hr>

## Systems to interact with:

### Freshbooks 
   - Accounting system for membership dues (Stripe used for payment processing) 
   - [API docs](https://www.freshbooks.com/api/start)
   - Uses OAuth for authentication
<br><br>

### Discourse 
   - Forum for member discussion 
   - [API docs](https://docs.discourse.org/)
   - `GET` calls only require API key and API user in headers
   - `POST` calls require API key, API user, and content-type in the headers
   - See verified example scripts in `/examples` directory
<br><br>

### Skedda 
   - Scheduling system for booking time at the space
   - Checked with CSM about API, they have integrations through Zapier, but no direct access endpoint.  May be able to reverse engineer to figure out endpoints and methods
<br><br>

### Mailchimp 
   - Email service for updates 
   - [API docs](https://mailchimp.com/developer/reference/)

<br><br>

### Key fob system 
   - Used for access into the space
   - We will need to research how to interact with this system 
<br><br>
<hr>

## About this repo
This is an open-source project for ATX Hackerspace.  Keep any API tokens or other private information stored in the `/private` directory which is ignored by git.  If you are interested in working on this project with us, please reach out to [it@atxhs.org](mailto:it@atxhs.org).
