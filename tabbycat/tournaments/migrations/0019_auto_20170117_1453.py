# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-17 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0018_auto_20161119_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='emoji',
            field=models.CharField(blank=True, choices=[('☕', '☕'), ('⛑', '⛑'), ('⛰', '⛰'), ('⛪', '⛪'), ('⛵', '⛵'), ('⛔', '⛔'), ('⛅', '⛅'), ('⛈', '⛈'), ('⛱', '⛱'), ('⛄', '⛄'), ('⚽', '⚽'), ('⛏', '⛏'), ('😁', '😁'), ('😂', '😂'), ('😄', '😄'), ('😆', '😆'), ('😉', '😉'), ('😊', '😊'), ('😎', '😎'), ('😍', '😍'), ('😘', '😘'), ('😇', '😇'), ('😐', '😐'), ('😏', '😏'), ('😥', '😥'), ('😜', '😜'), ('😖', '😖'), ('😷', '😷'), ('😲', '😲'), ('😞', '😞'), ('😭', '😭'), ('😰', '😰'), ('😱', '😱'), ('😳', '😳'), ('😵', '😵'), ('😡', '😡'), ('👿', '👿'), ('👩', '👩'), ('👴', '👴'), ('👵', '👵'), ('👶', '👶'), ('👮', '👮'), ('👷', '👷'), ('👸', '👸'), ('💂', '💂'), ('🎅', '🎅'), ('👼', '👼'), ('👰', '👰'), ('🙅', '🙅'), ('🙆', '🙆'), ('🙋', '🙋'), ('🙇', '🙇'), ('🙌', '🙌'), ('🙏', '🙏'), ('💃', '💃'), ('💑', '💑'), ('👪', '👪'), ('👫', '👫'), ('👬', '👬'), ('👭', '👭'), ('💪', '💪'), ('👆', '👆'), ('✊', '✊'), ('✋', '✋'), ('👊', '👊'), ('👌', '👌'), ('👍', '👍'), ('👎', '👎'), ('👐', '👐'), ('💅', '💅'), ('👂', '👂'), ('👃', '👃'), ('👅', '👅'), ('👄', '👄'), ('💘', '💘'), ('💔', '💔'), ('💖', '💖'), ('💌', '💌'), ('💧', '💧'), ('💣', '💣'), ('💥', '💥'), ('💦', '💦'), ('💨', '💨'), ('👓', '👓'), ('👔', '👔'), ('👙', '👙'), ('👜', '👜'), ('👟', '👟'), ('👠', '👠'), ('👒', '👒'), ('🎩', '🎩'), ('💄', '💄'), ('💍', '💍'), ('💎', '💎'), ('👻', '👻'), ('💀', '💀'), ('👽', '👽'), ('👾', '👾'), ('💩', '💩'), ('🐵', ''), ('🙈', ''), ('🙉', ''), ('🙊', ''), ('🐶', '🐶'), ('🐩', ''), ('🐯', '🐯'), ('🐴', '🐴'), ('🐮', '🐮'), ('🐷', '🐷'), ('🐑', '🐑'), ('🐭', '🐭'), ('🐹', '🐹'), ('🐰', '🐰'), ('🐻', '🐻'), ('🐨', '🐨'), ('🐼', '🐼'), ('🐔', '🐔'), ('🐦', '🐦'), ('🐧', '🐧'), ('🐸', '🐸'), ('🐍', '🐍'), ('🐲', '🐲'), ('🐳', '🐳'), ('🐟', '🐟'), ('🐙', '🐙'), ('🐚', '🐚'), ('🐝', '🐝'), ('🌸', '🌸'), ('🌹', '🌹'), ('🌻', '🌻'), ('🌷', '🌷'), ('🌱', ''), ('🌵', '🌵'), ('🍀', ''), ('🍁', '🍁'), ('🍇', '🍇'), ('🍉', '🍉'), ('🍊', '🍊'), ('🍋', '🍋'), ('🍌', '🍌'), ('🍍', '🍍'), ('🍎', '🍎'), ('🍑', '🍑'), ('🍒', '🍒'), ('🍓', '🍓'), ('🍅', '🍅'), ('🍆', '🍆'), ('🌽', '🌽'), ('🍄', '🍄'), ('🍞', '🍞'), ('🍔', '🍔'), ('🍕', '🍕'), ('🍙', ''), ('🍨', '🍨'), ('🍩', '🍩'), ('🍪', '🍪'), ('🍰', '🍰'), ('🍭', '🍭'), ('🍼', '🍼'), ('🍷', '🍷'), ('🍸', '🍸'), ('🍹', '🍹'), ('🍺', '🍺'), ('🍴', '🍴'), ('🌋', '🌋'), ('🏠', '🏠'), ('🏢', '🏢'), ('🏩', '🏩'), ('🌊', '🌊'), ('🎨', '🎨'), ('🚃', '🚃'), ('🚄', '🚄'), ('🚝', '🚝'), ('🚍', '🚍'), ('🚔', '🚔'), ('🚘', '🚘'), ('🚲', '🚲'), ('🚨', '🚨'), ('🚣', '🚣'), ('🚁', '🚁'), ('🚀', '🚀'), ('🚦', '🚦'), ('🚧', '🚧'), ('🚫', '🚫'), ('🚷', '🚷'), ('🚻', '🚻'), ('🚽', '🚽'), ('🚿', '🚿'), ('🛀', '🛀'), ('⏳', '⏳'), ('🌑', '🌑'), ('🌕', '🌕'), ('🌗', '🌗'), ('🌞', '🌞'), ('🌈', '🌈'), ('🌂', '🌂'), ('🌟', '🌟'), ('🔥', '🔥'), ('🎃', '🎃'), ('🎄', '🎄'), ('🎈', '🎈'), ('🎉', '🎉'), ('🎓', '🎓'), ('🎯', '🎯'), ('🎀', '🎀'), ('🏀', '🏀'), ('🏈', '🏈'), ('🎾', '🎾'), ('🎱', '🎱'), ('🎮', '🎮'), ('🎲', '🎲'), ('📣', '📣'), ('📯', ''), ('🔔', '🔔'), ('🎶', '🎶'), ('🎤', '🎤'), ('🎹', '🎹'), ('🎺', '🎺'), ('🎻', '🎻'), ('📻', '📻'), ('📱', '📱'), ('📞', '📞'), ('🔋', '🔋'), ('🔌', '🔌'), ('💾', '💾'), ('💿', '💿'), ('🎬', '🎬'), ('📷', '📷'), ('🔍', '🔍'), ('🔭', '🔭'), ('💡', '💡'), ('📕', '📕'), ('📰', '📰'), ('💰', '💰'), ('💸', '💸'), ('📦', ''), ('📫', '📫'), ('💼', '💼'), ('📅', '📅'), ('📏', '📏'), ('📐', '📐'), ('🔑', '🔑'), ('🔩', '🔩'), ('💊', ''), ('🔪', '🔪'), ('🔫', '🔫'), ('🚬', '🚬'), ('🏁', ''), ('🔮', '🔮'), ('❌', '❌'), ('❓', '❓'), ('🔞', '🔞'), ('🆒', '🆒'), ('🆗', '🆗'), ('🆘', '🆘'), ('😙', '😙'), ('😑', '😑'), ('😮', '😮'), ('😴', '😴'), ('😛', '😛'), ('😧', '😧'), ('😬', '😬'), ('🕵', '🕵'), ('🖕', '🖕'), ('🖖', '🖖'), ('👁', '👁'), ('🕶', '🕶'), ('🛍', '🛍'), ('🐿', '🐿'), ('🕊', '🕊'), ('🕷', '🕷'), ('🌶', '🌶'), ('🏛', '🏛'), ('🛢', '🛢'), ('🛎', '🛎'), ('🕰', '🕰'), ('🌡', '🌡'), ('🌤', '🌤'), ('🌧', '🌧'), ('🌩', '🌩'), ('🌪', '🌪'), ('🌫', '🌫'), ('🌬', '🌬'), ('🎖', '🎖'), ('🎗', '🎗'), ('🎞', '🎞'), ('🏷', '🏷'), ('🏅', '🏅'), ('🕹', '🕹'), ('🎙', '🎙'), ('🖥', '🖥'), ('🖨', '🖨'), ('🖲', '🖲'), ('🕯', '🕯'), ('🖋', '🖋'), ('🗑', '🗑'), ('🗡', '🗡'), ('🛡', '🛡'), ('🏳', '🏳'), ('🏴', '🏴'), ('🤗', '🤗'), ('🤔', '🤔'), ('🙄', '🙄'), ('🤐', '🤐'), ('🤓', '🤓'), ('🙃', '🙃'), ('🤒', '🤒'), ('🤕', '🤕'), ('🤑', '🤑'), ('🤘', '🤘'), ('📿', '📿'), ('🤖', '🤖'), ('🦁', '🦁'), ('🦄', '🦄'), ('🦀', '🦀'), ('🧀', '🧀'), ('🌭', '🌭'), ('🌮', '🌮'), ('🍿', '🍿'), ('🍾', '🍾'), ('🏏', '🏏'), ('🏐', '🏐'), ('🏓', '🏓'), ('🏹', '🏹')], max_length=2, null=True, unique=True, verbose_name='emoji'),
        ),
    ]