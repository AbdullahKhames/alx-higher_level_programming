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
	temp->n = number;

	while(next)
	{
		if (next->n < number)
		{
			next++;
			cuurent++;
		}
		else
		{
			temp->next = current->next;
			current->next = temp;
			break;
		}
	}
	return(temp);
}
