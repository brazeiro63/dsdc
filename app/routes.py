from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_babel import _
from .forms import LeadForm

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = LeadForm()
    if form.validate_on_submit():
        # Aqui você pode salvar o lead (ex: enviar por e-mail, salvar em banco, etc.)
        flash(_('Lead recebido com sucesso! Entraremos em contato em breve.'), 'success')
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form)
