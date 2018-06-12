from magi.forms import AccountForm as _AccountForm

############################################################
# Account

class AccountForm(_AccountForm):
    class Meta(_AccountForm.Meta):
        fields = ('i_website', 'c_groups')
