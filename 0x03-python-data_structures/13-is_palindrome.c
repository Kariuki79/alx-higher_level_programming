#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the head of the list
 *
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *reversed_half, *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	/* Find middle using slow and fast pointer */
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* Reverse second half */
	second_half = slow;
	reverse_listint(&second_half);
	reversed_half = second_half;

	/* Compare halves */
	temp = *head;
	while (reversed_half)
	{
		if (temp->n != reversed_half->n)
		{
			reverse_listint(&second_half); /* Restore list */
			return (0);
		}
		temp = temp->next;
		reversed_half = reversed_half->next;
	}

	/* Restore list and return */
	reverse_listint(&second_half);
	return (1);
}
