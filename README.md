Olark - Close.io integration
--------------------------

Uses Olark webhooks to push the chat transcripts as notes into Close.io.

Customize
--------------------------

Depending on the info you provide via the Olark's JS API, you need to
customize the way you identify leads. For example, if an email of a user is
known, you can first search for leads with that email (`/api/v1/lead/?query=email@example.com`),
gather the lead ids and then post notes for given leads.

Alternatively, you could set up the app to email you with a nicely formatted
chat transcript and then paste it into Close.io manually.
