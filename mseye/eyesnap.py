import mongoengine as me


class EyeSnap(me.Document):
    timestamp = me.DateTimeField(required=True)
    name = me.StringField(required=True)
