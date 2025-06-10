from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from app.forms import LeadForm
from app.models import Lead
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/index', methods=['GET', 'POST'])
def index():
    form = LeadForm()
    if form.validate_on_submit():
        # Criar um novo lead a partir dos dados do formulário
        lead = Lead(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            message=form.message.data
        )
        db.session.add(lead)
        db.session.commit()
        
        flash('Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('index.html', form=form)

# Rota para a página Quem Somos
@main_bp.route('/quem-somos')
def quem_somos():
    return render_template('quem_somos.html')

# API endpoint para receber leads via AJAX (opcional)
@main_bp.route('/api/leads', methods=['POST'])
def create_lead_api():
    data = request.json
    
    if not data.get('email'):
        return jsonify({"error": "Email é obrigatório"}), 400
    
    lead = Lead(
        name=data.get('name', ''),
        email=data.get('email'),
        phone=data.get('phone', ''),
        message=data.get('message', '')
    )
    
    db.session.add(lead)
    db.session.commit()
    
    return jsonify({"message": "Lead registrado com sucesso", "id": lead.id}), 201

# Rota para visualizar leads (protegida por autenticação em produção)
@main_bp.route('/admin/leads')
def view_leads():
    # Aqui você adicionaria autenticação em produção
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    return render_template('admin/leads.html', leads=leads)