@login_required
def volunteer_accept(request, volunteer_id):
    """ Accept an help from the volunteer_id """
    demandProposition = DemandProposition.objects.get(pk=volunteer_id)
    demand = demandProposition.demand

    if can_manage_branch_specific(demand.receiver, request.user, demand.branch):
        demandProposition.accepted = True
        demandProposition.save()

        subject = _("Je vous ai choisi pour '") + demand.title + "'"
	# ....
        body += '\n' + _('Description : ') + demand.description

        if demand.receiver.emergency_contacts.count() > 0:
            body += '\n' + _('En cas d\'incident durant cette tâche, voici les personnes à contacter :')
            for ec in demand.receiver.emergency_contacts.all():
                body += '\n' + _('Prénom :') + ' ' + ec.first_name
		# ...
                body += '\n' + _('Langues parlées :') + ' ' + ec.get_verbose_languages()
                body += '\n'
        body += demand.receiver.first_name
        pm_write(demand.receiver, demandProposition.user, subject, body)
        for vol in DemandProposition.objects.filter(demand=demand, accepted=False):
            vol.delete()

        demand.closed = True
        demand.km = demandProposition.km
        if not demand.km:
            demand.km = 0
        demand.donor = demandProposition.user
        demand.save()

        messages.add_message(request, messages.INFO, _('Vous avez accepté cette aide !'))
        return redirect(demand.get_absolute_url())
    return redirect('home')
