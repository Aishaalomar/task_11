class Profile (models.Model):
    USER_TYPES = [
        ('NONE', 'None')
        ('OWNER', 'Owner'),
        ('CUSTOMER', 'Customer')
    ]
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=8, USER_TYPES, default='NONE' )
    paci_no = models.CharField(max_length=12, null=True)
    civilID = models.CharField(max_length=12, null=True)
    profile_picture = models.ImageField()
    # You have to setup the media folder in settings 

    def __str__(self):
        return self.user.username