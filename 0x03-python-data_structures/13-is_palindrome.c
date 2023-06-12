#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * is_palindrome - function to check palindrome
 * @head: the list to check
 * Return: returns 0 if not
 *	and returns 1 if is
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *start;
	int counter = 0;
	int *arr;
	int i = 0;
	int j;

	if (!head)
		return -1;
	start = *head;
	current = *head;
	counter++;
	if(current->next != NULL)
	{
		next = current->next;
		counter++;
	}
	while (next->next != NULL)
	{
		current = next;
		next = next->next;
		counter++;
	}
	if (counter % 2 != 0)
		return 0;

	arr = malloc(sizeof(int) * counter);
	if (arr == NULL)
		return 0;
	for (; i< counter; i++)
	{
		arr[i] = start->n;
		start = start->next;
	}
	for (i = 0, j = counter - 1; i < counter/2; i++, j--)
	{
		if (!check_equal(arr[i],arr[j]))
		{
			return 0;
		}
	}
	
	return 1;


}
/**
 * check_equal - function test equality
 * @x: first arg
 * @y: second arg
 * Return 1 if true
 *	0 otherwise
 */
int check_equal(int x, int y)
{
	if (x == y)
		return 1;
	return 0;
}
