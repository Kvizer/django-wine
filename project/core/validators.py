# -*- coding: utf-8 -*-
import logging
from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

log = logging.getLogger(__name__)

non_numeric = RegexValidator(regex=u'^[a-zA-ZãÃäÄàÀâÂçÇéÉèÈêÊëËîíÍÎïÏôóÓöÖÔûÛÙúÚùÙüÛÿŶñÑæÆœŒ -.\']*$',
                                      message=_('Expression should not contain numeric values'),
                                      code='no_numeric_expected'
                            )

numeric_only = RegexValidator(regex='^[0-9\s-]*$',
                                      message=_('Expression contains letters'),
                                      code='numeric_only_expected'
                             )

price = RegexValidator(regex='^\d+\.?\d{0,2}$',
                                      message=_(u'Not a valid price. 2 decimals maximum and numbers only is allowed.'),
                                      code='not_price_formatted'
                      )
price_too_high = RegexValidator(regex='^\d{1,5}\.?\d+$',
                                      message=_('This price seems too high. Please make sure it is correct.'),
                                      code='price_too_high'
                               )

percentage = RegexValidator(regex='^\d{1,2}\.?\d{0,2}$',
                                      message=_('This is not a valid percentage. Maximum is 100% and only put 2 decimals maximum.'),
                                      code='not_percentage'
                           )

def validate_future_date(value):
    # formatted_date = datetime.strptime(value,"%Y%m%d")
    if value > timezone.now().date():
        msg = _('Invalid Date. This date is in the future.')
        code = 'invalid_date'
        raise ValidationError(msg, code)
