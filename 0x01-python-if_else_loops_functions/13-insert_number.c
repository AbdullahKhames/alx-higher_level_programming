#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stddef.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *current;
	listint_t *next;

	(void) current;
	(void) next;
	if (!head)
		return NULL;

	if(*head == NULL)
	{
		current = malloc(sizeof(listint_t));
		next = malloc(sizeof(listint_t));
	}
	else
	{
		current = *head;
		next = *head;
	}
	temp = malloc(sizeof(listint_t));
	if (!temp)
		return NULL;
	temp->n = number;
	temp->next = NULL;

	if (*head == NULL || number < (*head)->n) {
		temp->next = *head;
		*head = temp;
	} else {
		listint_t *current = *head;
		while (current->next && current->next->n < number) {
		current = current->next;
	}
	temp->next = current->next;
	current->next = temp;
}
	return(temp);
}
