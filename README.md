# ATXHS BatPass

Discourse thread at https://yo.atxhs.org/t/revamping-our-internal-systems/300

The vision – **all admin interactions with account(s) occur through the LDAP**. LDAP is the source of truth for all member info including active billing, B-share, contact info, etc (i.e. admins do not directly interact with subsystems like Freshbooks to update accounts). Accurate info, easily accessible.


Here's what the basic workflow would look like for the base model created which we can build further upon.
[BatPass workflow](BatPass/images/ATXHS BatPass.png)

Link to Google drawing [here](https://docs.google.com/drawings/d/1yIYogNvRNthOQkoszzCV3sKi9nQr5vJnzmHsZl3sID4/edit?usp=sharing)


### Systems to interact with:
1. **Freshbooks** - accounting system for membership dues (Stripe used for payment processing) [API docs](https://www.freshbooks.com/api/start)
2. **Discourse** - forum for member discussion [API docs](https://docs.discourse.org/)
3. **Skedda** - scheduling system for booking time at the space
   - Checked with CSM about API, they have integrations through Zapier, but no direct access endpoint.  May be able to reverse engineer to figure out endpoints and methods
4. **Mailchimp** - email service for updates [API docs](https://mailchimp.com/developer/reference/)
   - We will need to update account to include API package when we are ready to roll out
5. **Key fob system** - used for access into the space
   - We will need to research how to interact with this system 



