#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *nex;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	nex = current->next;

	while (current != NULL && nex->next != NULL
		&& nex->next->next != NULL)
	{
		if (current == nex)
			return (1);
		current = current->next;
		nex = nex->next->next;
	}
	return (0);
}

