import mongoengine as me

class EyeSnap(me.Document):
    timestamp = me.DateTimeField(required=True)
    path = me.StringField(required=True)
