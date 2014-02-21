import datetime

def User(db.DynamicDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=True)
    openid = db.IntField(required=True, unique=True)

    def __unicode__(self):
        return self.name

    meta = {
        'indexes' : ['-created_at', 'openid'],
        'ordering' : ['-created_at']
    }


user
{
	"userId" : userId,
	"name" : name,
	"importance" : 1(user), 2(cooluser), 3(admin),
	"avatar" : avatarUrl,
	"votes" : [
		{
			"voteId" : rateId1
		},
		{
			"voteId" : rateId2
		}
			  ]

}