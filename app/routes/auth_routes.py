from flask import Blueprint, render_template, redirect, url_for, session
from app.forms.trainer_form import TrainerForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def index():
    if session.get('trainer'):
        return redirect(url_for('pokemon.listado'))

    form = TrainerForm()
    if form.validate_on_submit():
        session['trainer'] = form.trainer.data.strip()
        return redirect(url_for('pokemon.listado'))
        
    return render_template(
        'index.html',
        form=form,
        proyecto="Batallas Pokemon",
        nombre="Abdullah",
        año=2026
    )

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))