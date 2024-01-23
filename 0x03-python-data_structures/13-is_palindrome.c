#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: double pointer to the head
 *
 * Return: nothing
*/
void reverse_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: double pointer to the head
 *
 * Return: nothing
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *second_half = NULL;
	listint_t *first_current, *second_current;

	/* empty or a list with a single node is considered a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* find the middle of the list by slow and fast pointer technique */
	slow = fast = prev_slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	/* if odd number of nodes*/
	if (fast != NULL)
		slow = slow->next;

	/* Reverse the second half of the linked list */
	second_half = slow;
	prev_slow->next = NULL;
	reverse_list(&second_half);

	/* compare the two halfs of the list */
	first_current = *head;
	second_current = second_half;
	while (first_current != NULL && second_current != NULL)
	{
		if (first_current->n != second_current->n)
			return (0);

		first_current = first_current->next;
		second_current = second_current->next;
	}
	return (1);
}
